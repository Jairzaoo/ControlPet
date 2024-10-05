import { ApplicationConfig } from '@angular/core';
import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import { provideAuth, getAuth } from '@angular/fire/auth';
import { importProvidersFrom } from '@angular/core';
import { environment } from '../environments/environment';
import { FormsModule } from '@angular/forms';
import { AuthService } from './auth/auth.service';  // Corrigindo o caminho do AuthService

export const appConfig: ApplicationConfig = {
  providers: [
    importProvidersFrom(provideFirebaseApp(() => initializeApp(environment.firebaseConfig))),
    importProvidersFrom(provideAuth(() => getAuth())),
    importProvidersFrom(FormsModule),
    AuthService  // O AuthService será registrado automaticamente por estar em 'root'
  ]
};
