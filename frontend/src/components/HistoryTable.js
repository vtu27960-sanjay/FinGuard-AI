import React, { useEffect, useState } from "react";
import API from "../services/api";

function HistoryTable() {
    const [history, setHistory] = useState([]);

    useEffect(() => {
        fetchHistory();
    }, []);

    const fetchHistory = async () => {
        try {
            const response = await API.get("/history");
            setHistory(response.data);
        } catch (error) {
            console.error("Error fetching history:", error);
        }
    };

    return (
        <div className="card mt-4 p-4">
            <h3>Transaction History</h3>

            <table className="table table-bordered">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Amount</th>
                        <th>Prediction</th>
                    </tr>
                </thead>

                <tbody>
                    {history.map((item) => (
                        <tr key={item.id}>
                            <td>{item.id}</td>
                            <td>{item.amount}</td>
                            <td>{item.prediction}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default HistoryTable;