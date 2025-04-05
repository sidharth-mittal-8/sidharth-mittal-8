# Django/Flask Codespace Project - /htop Endpoint

This project is built on GitHub Codespaces using either Django or Flask. It provides a `/htop` endpoint that returns system information including:

- Full Name
- System Username
- Server Time in IST
- Output from the `top` command (first 10–20 lines)

The endpoint is meant to stay live without shutting down the Codespace.

---

## Task Instructions

1. Create an account on https://github.com  
2. Create a codespace using https://github.com/codespaces  
3. Set Codespace timeout to **240 minutes** (maximum)  
4. Start a new Codespace  
5. Create a Django or Flask application  
6. Implement an endpoint `/htop`  
7. Make sure the app is served on a public port  
8. DO NOT stop the Codespace — it must remain active so the endpoint keeps running  
9. Test the `/htop` endpoint in an incognito browser tab before submission  

---

## Endpoint Output

The `/htop` page should show the following:

- **Name** – your full name  
- **Username** – system username from the server  
- **Server Time in IST** – Indian Standard Time  
- **Top Output** – output of the `top` command (formatted as HTML)  

---

## Example Output

