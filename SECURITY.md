# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly:

1. **Do NOT** open a public GitHub issue for security vulnerabilities
2. Contact the maintainers privately via Discord or email
3. Provide detailed information about the vulnerability
4. Allow reasonable time for a fix before public disclosure

## Security Best Practices

### For Users

- **Never commit `.env` files** - Always use `.env.example` as a template
- **Regenerate tokens immediately** if they are accidentally exposed
- **Use minimal bot permissions** - Only grant permissions the bot actually needs
- **Keep dependencies updated** - Run `pip install --upgrade -r requirements.txt` regularly

### Bot Permissions

This bot requires minimal permissions:
- `Send Messages` - To respond to commands
- `Embed Links` - To send rich embeds
- `Attach Files` - To send exported files
- `Read Message History` - For context in channels
- `Use Slash Commands` - For slash command functionality

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `DISCORD_TOKEN` | Yes | Bot token from Discord Developer Portal |
| `GUILD_ID` | No | Server ID for faster command sync |
| `OUTPUT_CHANNEL_ID` | No | Channel ID for scheduled reminders |

## Security Measures Implemented

- No user input is executed as code
- No database queries (no SQL injection risk)
- No external API calls with user data
- Slash commands validated by Discord
- Secrets excluded from version control via `.gitignore`
- Error messages do not leak sensitive information
