import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PostLoginComponent } from './post-login/post-login.component';
import { HomeComponent } from './home/home.component'; // Se existir uma página home

export const routes: Routes = [
  { path: 'login', component: LoginComponent },        // Rota para login
  { path: 'post-login', component: PostLoginComponent }, // Rota para pós-login
  { path: '', redirectTo: '/login', pathMatch: 'full' }, // Redireciona para login como página inicial
  { path: '**', component: HomeComponent } // Para rotas não encontradas (opcional)
];
