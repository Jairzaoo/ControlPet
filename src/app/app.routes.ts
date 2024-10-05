// src/app/app.routes.ts
import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PostLoginComponent } from './post-login/post-login.component';  // Novo componente

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'post-login', component: PostLoginComponent },  // Rota pós-login
  { path: '', redirectTo: '/login', pathMatch: 'full' },  // Redireciona para o login por padrão
];
