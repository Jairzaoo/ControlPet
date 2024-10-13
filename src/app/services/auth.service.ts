import { Injectable } from '@angular/core';
import { getAuth, signInWithEmailAndPassword } from '@angular/fire/auth';

@Injectable({
<<<<<<< HEAD
  providedIn: 'root'  // Isso torna o AuthService disponível globalmente
})
export class AuthService {

=======
  providedIn: 'root'
})
export class AuthService {
>>>>>>> 47a6f47 ( )
  constructor() {}

  login(email: string, password: string) {
    const auth = getAuth();
    return signInWithEmailAndPassword(auth, email, password);
  }
}
