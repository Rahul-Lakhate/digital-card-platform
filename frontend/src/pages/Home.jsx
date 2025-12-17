import { api } from "../services/api";

export default function Home() {
  const pay = async () => {
    const { data } = await api.post("/payment/create-order");
    const rzp = new window.Razorpay({
      key: "RAZORPAY_KEY",
      order_id: data.id,
      handler: () => alert("Payment Success")
    });
    rzp.open();
  };

  return <button onClick={pay}>Create Digital Card</button>;
}
