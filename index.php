<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Prices</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Live Crypto Prices</h1>
    <table>
        <tr>
            <th>Currency</th>
            <th>Price (USD)</th>
        </tr>
        <?php
        $db = new SQLite3('/Applications/MAMP/htdocs/cryptoProject/crypto_prices.db');

        $results = $db->query('SELECT name, value, time FROM crypto ORDER BY time DESC LIMIT 2');
        while ($row = $results->fetchArray()) {
            echo "<tr><td>{$row['name']}</td><td>\${$row['value']}</td></tr>";
        }
        ?>
    </table>
</body>
</html>