import axios from "axios";

// URL CONFIGURATION
let apiFlask = "http://localhost:5005/";

export const API_URL_FLASK = apiFlask;

const api = axios.create();
api.defaults.baseURL = API_URL_FLASK;

export default api;
