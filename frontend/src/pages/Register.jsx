import { useState } from "react";
import {
    Link,
    useNavigate
} from "react-router-dom";

import api from "../services/api";
import "../App.css";

export default function Register() {

    const navigate = useNavigate();

    const [name, setName] =
        useState("");

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [confirmPassword,
        setConfirmPassword] =
        useState("");

    const [loading,
        setLoading] =
        useState(false);

    const handleRegister = async (e) => {

        e.preventDefault();

        if (
            password !==
            confirmPassword
        ) {
            alert(
                "Passwords do not match"
            );
            return;
        }

        setLoading(true);

        try {

            await api.post(
                "/auth/register",
                {
                    name,
                    email,
                    password
                }
            );

            alert(
                "Registration Successful"
            );

            navigate("/");

        }
        catch (error) {

            alert(
                error.response?.data?.detail ||
                "Registration Failed"
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
                    Create Account
                </h1>

                <p className="auth-subtitle">
                    Join your AI RAG Assistant
                </p>

                <form
                    className="auth-form"
                    onSubmit={handleRegister}
                >

                    <input
                        type="text"
                        placeholder="Full Name"
                        value={name}
                        onChange={(e) =>
                            setName(
                                e.target.value
                            )
                        }
                        required
                    />

                    <input
                        type="email"
                        placeholder="Email Address"
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
                        placeholder="Password"
                        value={password}
                        onChange={(e) =>
                            setPassword(
                                e.target.value
                            )
                        }
                        required
                    />

                    <input
                        type="password"
                        placeholder="Confirm Password"
                        value={confirmPassword}
                        onChange={(e) =>
                            setConfirmPassword(
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
                                ? "Creating Account..."
                                : "Register"
                        }
                    </button>

                </form>

                <div
                    style={{
                        textAlign:
                            "center",
                        marginTop:
                            "20px",
                        color:
                            "#94a3b8"
                    }}
                >
                    Already have an account?

                    <br />

                    <Link
                        to="/"
                        style={{
                            color:
                                "#60a5fa",
                            textDecoration:
                                "none",
                            fontWeight:
                                "600"
                        }}
                    >
                        Login Here
                    </Link>

                </div>

            </div>

        </div>
    );
}