import { initializeApp } from "firebase/app";
import { 
  getAuth, GoogleAuthProvider, signInWithPopup, signOut, onAuthStateChanged 
} from "firebase/auth";
import { getFirestore, doc, setDoc, getDoc, updateDoc, arrayUnion } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyAeMU-iDX1Ws-j2ZIbNYWKwxnZ2LgxZVg0",
  authDomain: "innovnutribite.firebaseapp.com",
  projectId: "innovnutribite",
  storageBucket: "innovnutribite.firebasestorage.app",
  messagingSenderId: "1029629190173",
  appId: "1:1029629190173:web:b46662166242ae1a6d26f4",
  measurementId: "G-FL1J4C0T3H"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
const db = getFirestore(app);

export { auth, provider, signInWithPopup, signOut, onAuthStateChanged, db, doc, setDoc, getDoc, updateDoc, arrayUnion };
