// src/app/login/login.component.ts
import { Component } from '@angular/core';
import { Router } from '@angular/router';  // Para navegação pós-login
import { AuthService } from '../services/auth.service';  // Importa o serviço de autenticação

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  standalone: true  // Tornar o componente standalone
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  // Função de login
  login() {
    this.authService.login(this.email, this.password)
      .then(() => {
        console.log('Login successful');
        // Redireciona para a tela de pós-login após o sucesso
        this.router.navigate(['/post-login']);
      })
      .catch(error => {
        this.errorMessage = error.message;
        console.error('Login failed:', error);
      });
  }
}
