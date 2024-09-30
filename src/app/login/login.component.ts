// src/app/login/login.component.ts
import { Component } from '@angular/core';
import { AuthService } from '../services/auth.service'; // Ajuste o caminho conforme necessário

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  standalone: true // Adicione esta linha se você estiver usando componentes standalone
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService) {}

  login() {
    this.authService.login(this.email, this.password)
      .then(() => {
        console.log('Login successful');
        // Redirecionar para outra rota após o login, se necessário
      })
      .catch(error => {
        this.errorMessage = error.message;
        console.error('Login failed:', error);
      });
  }
}
