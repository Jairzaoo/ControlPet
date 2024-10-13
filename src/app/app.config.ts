import { ApplicationConfig } from '@angular/core';
import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import { provideAuth, getAuth } from '@angular/fire/auth';
import { importProvidersFrom } from '@angular/core';
import { environment } from '../environments/environment';
<<<<<<< HEAD
import { FormsModule } from '@angular/forms';
import { AuthService } from './auth/auth.service';  // Corrigindo o caminho do AuthService
=======
import { AuthService } from './auth/auth.service'; // Corrija o caminho se necessário
>>>>>>> 47a6f47 ( )

export const appConfig: ApplicationConfig = {
  providers: [
    importProvidersFrom(provideFirebaseApp(() => initializeApp(environment.firebaseConfig))),
    importProvidersFrom(provideAuth(() => getAuth())),
<<<<<<< HEAD
    importProvidersFrom(FormsModule),
    AuthService  // O AuthService será registrado automaticamente por estar em 'root'
=======
    AuthService  // O AuthService será registrado automaticamente
>>>>>>> 47a6f47 ( )
  ]
};
