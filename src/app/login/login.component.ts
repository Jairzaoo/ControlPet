import { Component } from '@angular/core';
import { Router } from '@angular/router';
<<<<<<< HEAD
import { AuthService } from '../auth/auth.service';  // Corrigindo o caminho de importação
=======
import { AuthService } from '../auth/auth.service'; // Verifique o caminho
>>>>>>> 47a6f47 ( )

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.email, this.password).then(() => {
      this.router.navigate(['/post-login']);
    }).catch((err: any) => {
      this.errorMessage = 'Login falhou. Tente novamente.';
    });
  }
}
