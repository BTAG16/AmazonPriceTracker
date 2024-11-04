# AmazonPriceTracker

AmazonPriceTracker is a Python script designed to monitor the price of a specified Amazon product. When the price of the product drops below a set target, the script sends an email alert to notify you.

## Features
- Scrapes the price of a product from Amazon.
- Compares the current price with a target price.
- Sends an email notification when the price drops below the target.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AmazonPriceTracker.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables by creating a `.env` file in the project directory:
   ```plaintext
   SENDER=your_email@gmail.com
   PASSWORD=your_email_password
   RECEIVER=receiver_email@gmail.com
   ```
   Replace these with the appropriate email credentials.

## Usage

1. Update the `amazon_URL` and `target_price` in `main.py`:
   - `amazon_URL`: The URL of the Amazon product you want to track.
   - `target_price`: The price threshold for sending an alert.
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will continuously check the product's price every specified interval (modify `time.sleep()` if necessary).

## Environment Variables

The following environment variables need to be defined in your `.env` file:

- `SENDER`: The email address from which the price alerts will be sent.
- `PASSWORD`: The password for the sender's email account.
- `RECEIVER`: The email address where price alerts will be received.

## Notes
- Be aware that Amazon may restrict repeated requests from scraping scripts.
- Use a `User-Agent` header in `amazon_headers` to simulate a real browser.
- get the `User-Agent` by pasting [https://httpbin.org/headers] in your browser.

## License
This project is licensed under the MIT License.

## Contact 
You can contact me via [rumeighoraye@gmail.com] or [LinkedIn](https://www.linkedin.com/in/cosmos-junior-ighoraye-4a8109239/)
