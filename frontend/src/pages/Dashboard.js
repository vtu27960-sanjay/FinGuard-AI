import React from "react";
import Navbar from "../components/Navbar";
import FraudForm from "../components/FraudForm";
import HistoryTable from "../components/HistoryTable";
import DashboardCards from "../components/DashboardCards";
import Charts from "../components/Charts";
import Chatbot from "../components/Chatbot";
import Footer from "../components/Footer";
function Dashboard() {
    return (
        <div>
            <Navbar />

            <div className="container mt-4">

                <h2 className="text-center mb-4">
                    FinGuard AI Dashboard
                </h2>

                <DashboardCards />

                <FraudForm />

                <HistoryTable />
                <Chatbot />

                {/* Charts Section */}
                <Charts />

            </div>
        </div>
    );
}
<Footer />


export default Dashboard;