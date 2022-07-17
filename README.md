# Hcaptcha-Identify-Node
A Hcaptcha Identify Node that identifies images. 

# Setup
```python
pip3 install -r requirements.txt
```
# Run
```python
python3 main.py
```
And then the server would run in http://localhost:5000

In your gen's config file

```json
{
  "solver_licence": "API-VK26SKC",
  "server_port": 3000,
  "softban": true,
  "dev_mode": true,
  "image_api": {
    "address": "localhost",
    "port": 5000,
    "skid" : "node01.proxies.gay",
    "skiidedport": 1337
  },

  "drop_req": false
}
```

Edit it like this. So address is localhost and port is 5000

