import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';

bootstrapApplication(AppComponent, {
<<<<<<< HEAD
  providers: [provideRouter(routes)]  // Configura as rotas aqui
=======
  providers: [provideRouter(routes)]
>>>>>>> 47a6f47 ( )
});
