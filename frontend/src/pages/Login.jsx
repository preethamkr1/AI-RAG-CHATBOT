import { useState } from "react";
import {
    Link,
    useNavigate
} from "react-router-dom";

import api from "../services/api";
import "../App.css";

export default function Login() {

    const navigate = useNavigate();

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const handleLogin = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const response =
                await api.post(
                    "/auth/login",
                    {
                        email,
                        password
                    }
                );

            localStorage.setItem(
                "token",
                response.data.access_token
            );

            navigate(
                "/dashboard"
            );

        }
        catch (error) {

            alert(
                error.response?.data?.detail ||
                "Login Failed"
            );
        }

        setLoading(false);
    };

    return (

        <div className="page-container">

            <div className="auth-card">

                <div className="logo-circle">
                    🤖
                </div>

                <h1 className="auth-title">
                    Welcome Back
                </h1>

                <p className="auth-subtitle">
                    Login to your AI RAG Assistant
                </p>

                <form
                    className="auth-form"
                    onSubmit={handleLogin}
                >

                    <input
                        type="email"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) =>
                            setEmail(
                                e.target.value
                            )
                        }
                        required
                    />

                    <input
                        type="password"
                        placeholder="Enter your password"
                        value={password}
                        onChange={(e) =>
                            setPassword(
                                e.target.value
                            )
                        }
                        required
                    />

                    <button
                        className="auth-button"
                        type="submit"
                    >
                        {
                            loading
                            ? "Logging in..."
                            : "Login"
                        }
                    </button>

                </form>

                <div
                    style={{
                        textAlign: "center",
                        marginTop: "20px",
                        color: "#94a3b8"
                    }}
                >
                    Don't have an account?
                    <br />

                    <Link
                        to="/register"
                        style={{
                            color: "#60a5fa",
                            textDecoration: "none",
                            fontWeight: "600"
                        }}
                    >
                        Create Account
                    </Link>

                </div>

            </div>

        </div>
    );
}