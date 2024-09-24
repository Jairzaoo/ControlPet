import { importProvidersFrom } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';


export const appConfig = {
  providers: [
    importProvidersFrom(BrowserModule),
      ]
};
