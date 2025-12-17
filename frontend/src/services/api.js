import axios from "axios";

export const api = axios.create({
  baseURL: "https://your-render-url.onrender.com"
});
