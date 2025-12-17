import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Card from "./pages/Card";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/card/:slug" element={<Card />} />
      </Routes>
    </BrowserRouter>
  );
}
