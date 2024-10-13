import { Routes } from '@angular/router';
<<<<<<< HEAD
import { LoginComponent } from './login/login.component';
import { PostLoginComponent } from './post-login/post-login.component';
import { HomeComponent } from './home/home.component'; // Se existir uma página home
=======
import { LoginComponent } from '/login/login.component';
import { PostLoginComponent } from './post-login/post-login.component';
import { HomeComponent } from './app/app.component'; // Se existir uma página home
>>>>>>> 47a6f47 ( )

export const routes: Routes = [
  { path: 'login', component: LoginComponent },        // Rota para login
  { path: 'post-login', component: PostLoginComponent }, // Rota para pós-login
  { path: '', redirectTo: '/login', pathMatch: 'full' }, // Redireciona para login como página inicial
  { path: '**', component: HomeComponent } // Para rotas não encontradas (opcional)
];
