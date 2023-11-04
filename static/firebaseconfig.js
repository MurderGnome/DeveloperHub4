// firebaseConfig.js

// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getDatabase } from "firebase/database";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDbRzICdk7-rbhi67OtnwSfIkVZI6K-crk",
    authDomain: "developer-hub-dd6f1.firebaseapp.com",
    databaseURL: "default.firebaseio.com",
    projectId: "developer-hub-dd6f1",
    storageBucket: "developer-hub-dd6f1.appspot.com",
    messagingSenderId: "852235384470",
    appId: "1:852235384470:web:54c537d81e743ff57634b7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize services
const auth = getAuth(app);
const database = getDatabase(app);
const firestore = getFirestore(app);
const storage = getStorage(app);

// Export services for use in other files
export { auth, database, firestore, storage };
