import { TelegramClient } from "telegram";
import { StringSession } from "telegram/sessions/index.js";
import input from "input"; // npm install input

const apiId = parseInt(await input.text("Enter your API ID: "));
const apiHash = await input.text("Enter your API Hash: ");
const botToken = await input.text("Enter your Bot Token: ");
const stringSession = new StringSession(""); // Empty session

console.log("\nGenerating session...");

const client = new TelegramClient(stringSession, apiId, apiHash, {
    connectionRetries: 5,
});

try {
    await client.start({
        botAuthToken: botToken,
    });

    console.log("\n== Your Bot String Session ==");
    console.log(client.session.save());
    console.log("\nKeep this string safe. You can use it to log in your bot later.");
    process.exit(0);
} catch (error) {
    console.error("\nError:", error.message || error);
    process.exit(1);
}
