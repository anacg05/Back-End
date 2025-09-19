import { Injectable , signal} from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, tap } from "rxjs";
import { environment } from "../environments/environments";

type TokenPair = {access: string; refresh?: string}

const storage = {
    get: (k: string) => (typeof localStorage !== 'undefined' ? localStorage.getItem(k): null)
    
}