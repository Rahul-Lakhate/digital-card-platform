import { useParams } from "react-router-dom";

export default function Card() {
  const { slug } = useParams();
  return <h1>Digital Card: {slug}</h1>;
}
