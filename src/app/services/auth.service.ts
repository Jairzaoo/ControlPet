import { Injectable } from '@angular/core';
import { getAuth, signInWithEmailAndPassword } from '@angular/fire/auth';

@Injectable({
  providedIn: 'root'  // Isso torna o AuthService disponível globalmente
})
export class AuthService {

  constructor() {}

  login(email: string, password: string) {
    const auth = getAuth();
    return signInWithEmailAndPassword(auth, email, password);
  }
}
