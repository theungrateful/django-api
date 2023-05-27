import React, { useState } from "react";
import { Form, Button} from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";


function LoginForm() {
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);

    const handleSubmit = (event) => {
        event.preventDefault();
        const loginForm = event.currentTarget;

        if (loginForm.checkValidity() === false) {
            event.stopPropagation();
        }

        setValidated(true);

        const data = {
            email: form.email,
            password: form.password,
        };

        axios
            .post("http://localhost:8000/api/auth/login/", data)
            .then((res) => {
                localStorage.setItem("auth.login", JSON.stringify({
                    access: res.data.access,
                    refresh: res.data.refresh,
                    user: res.data.user,
            }));

            navigate("/");

        })
        .catch((err) => {
            if (err.message){
            setError(err.message)
            }
        });
    };

    return (
        <Form
          id="registration-form"
          className="border p-4 rounded"
          noValidate
          validated={validated}
          onSubmit={handleSubmit}
          data-testid="login-form"
        >
          <Form.Group className="mb-3">
            <Form.Label>E-mail</Form.Label>
            <Form.Control
              value={form.email}
              data-testid="email-field"
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              required
              type="text"
              placeholder="Enter email"
            />
            <Form.Control.Feedback type="invalid">
              This file is required.
            </Form.Control.Feedback>
          </Form.Group>
    
          <Form.Group className="mb-3">
            <Form.Label>Password</Form.Label>
            <Form.Control
              value={form.password}
              data-testid="password-field"
              minLength="8"
              onChange={(e) => setForm({ ...form, password: e.target.value })}
              required
              type="password"
              placeholder="Password"
            />
            <Form.Control.Feedback type="invalid">
              Please provide a valid password.
            </Form.Control.Feedback>
          </Form.Group>
    
          <div className="text-content text-danger">{error && <p>{error}</p>}</div>
    
          <Button
            disabled={!form.password || !form.email}
            variant="primary"
            type="submit"
          >
            Submit
          </Button>
        </Form>
      );
}
    
export default LoginForm;
