# Crypto Signal Bot

Bot giám sát và cảnh báo tín hiệu giao dịch tiền điện tử qua Telegram. Hiện tại, bot hỗ trợ cảnh báo khi RSI của BTC giảm dưới ngưỡng cài đặt (mặc định là 30).

## Tính năng

- Kết nối Binance qua CCXT để lấy dữ liệu giá theo thời gian thực
- Tính toán chỉ báo RSI sử dụng thư viện TA
- Gửi cảnh báo qua Telegram khi có tín hiệu
- Có thể tùy chỉnh cặp tiền, khung thời gian và ngưỡng RSI

## Yêu cầu

- Python 3.8+
- Các thư viện trong file requirements.txt
- Tài khoản Binance (API key và Secret key)
- Bot Telegram đã được tạo

## Cài đặt

1. Clone repository:
```
git clone https://github.com/your-username/crypto-signal-bot.git
cd crypto-signal-bot
```

2. Cài đặt các thư viện yêu cầu:
```
pip install -r requirements.txt
```

3. Tạo file `.env` từ file mẫu:
```
cp .env-example .env
```

4. Cập nhật các thông tin trong file `.env` với API key của bạn:
```
# Binance API keys
BINANCE_API_KEY=your_binance_api_key
BINANCE_SECRET_KEY=your_binance_secret_key

# Telegram Bot
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id

# Bot settings
RSI_THRESHOLD=30
RSI_TIMEFRAME=1h
COIN_SYMBOL=BTC/USDT

# Proxy settings (optional)
PROXY_URL=
PROXY_USERNAME=
PROXY_PASSWORD=
```

## Hướng dẫn tạo Telegram Bot

1. Mở Telegram và tìm kiếm `@BotFather`
2. Gửi lệnh `/newbot` và làm theo hướng dẫn
3. Sau khi tạo xong, bạn sẽ nhận được `TELEGRAM_BOT_TOKEN`
4. Để lấy `TELEGRAM_CHAT_ID`, tạo một nhóm chat, thêm bot vào nhóm, và sử dụng API để lấy chat ID

## Cấu hình Proxy (Tùy chọn)

Nếu bạn cần sử dụng proxy để kết nối Telegram, hãy cấu hình trong file `.env`:

```
PROXY_URL=http://proxy-server:8080
PROXY_USERNAME=your_username  # Nếu proxy yêu cầu authentication
PROXY_PASSWORD=your_password  # Nếu proxy yêu cầu authentication
```

Xem hướng dẫn chi tiết trong file [PROXY_GUIDE.md](PROXY_GUIDE.md).

### Test kết nối proxy

```
python test_proxy.py
```

## Chạy Bot

### Bot giám sát RSI:
```
python main.py
```

### Bot Telegram chat:
```
python telegram_bot.py
```

Bot sẽ tự động chạy và gửi cảnh báo qua Telegram khi RSI của BTC giảm dưới ngưỡng đã cài đặt.

## Thêm cặp tiền khác

Bạn có thể thay đổi cặp tiền trong file `.env` bằng cách sửa biến `COIN_SYMBOL`, ví dụ:
```
COIN_SYMBOL=SOL/USDT
```

## Tùy chỉnh cảnh báo

Sửa ngưỡng RSI và khung thời gian trong file `.env`:
```
RSI_THRESHOLD=35  # Thay đổi ngưỡng RSI
RSI_TIMEFRAME=4h  # Thay đổi khung thời gian (1m, 5m, 15m, 1h, 4h, 1d)
```

## Đóng góp

Vui lòng gửi pull request hoặc báo lỗi qua Issues.

## License

MIT 