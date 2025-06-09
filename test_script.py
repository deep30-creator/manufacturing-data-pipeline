import socket

host = "db.xuxdfohhcilfxvrowyxq.supabase.co"
port = 5432

try:
    socket.create_connection((host, port), timeout=5)
    print("✅ Network OK: Able to reach Supabase host on port 5432")
except Exception as e:
    print("❌ Network Error:", e)
