from typing import List

from fastapi_mail import MessageSchema, FastMail
from pydantic import EmailStr

from core.settings import mail_conf


async def sending_email_(subject: str, html: str, recipients: List[EmailStr]):
    """ Function to send email """
    message = MessageSchema(
        subject=subject,
        recipients=recipients,  # List of recipients, as many as you can pass
        body=html,
        subtype="html"
    )

    fm = FastMail(mail_conf)
    await fm.send_message(message)
