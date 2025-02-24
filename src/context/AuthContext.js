import { createContext, useContext, useEffect, useState } from "react";
import { 
  auth, 
  provider, 
  signInWithPopup, 
  signOut, 
  db, 
  doc, 
  setDoc, 
  getDoc, 
  onAuthStateChanged 
} from "../firebase";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Listen for auth state changes
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, async (currentUser) => {
      if (currentUser) {
        await saveUserToFirestore(currentUser);
        setUser(currentUser);
      } else {
        setUser(null);
      }
      setLoading(false);
    });

    return () => unsubscribe();
  }, []);

  // Save user data to Firestore if not exists
  const saveUserToFirestore = async (userData) => {
    try {
      const userDocRef = doc(db, "users", userData.uid);
      const userDoc = await getDoc(userDocRef);

      if (!userDoc.exists()) {
        await setDoc(userDocRef, { chatHistory: [] });
      }
    } catch (error) {
      console.error("Error saving user to Firestore:", error);
    }
  };

  // Google Sign-in
  const loginWithGoogle = async () => {
    try {
      const result = await signInWithPopup(auth, provider);
      setUser(result.user);
    } catch (error) {
      console.error("Google login failed:", error);
    }
  };

  // Logout function
  const logout = async () => {
    try {
      await signOut(auth);
      setUser(null);
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return (
    <AuthContext.Provider value={{ user, loginWithGoogle, logout, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

// Custom Hook
export const useAuth = () => useContext(AuthContext);
