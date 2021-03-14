from src.lib import endpoints
from src import constants
from src.bot.commands import helpers


def handle_match_details_callback(update, context):
    query = update.callback_query

    match_id = int(query.data.replace("match ", ""))

    response, status_code = endpoints.get_match_by_id(match_id)

    if status_code != constants.HTTP_STATUS_CODES.OK.value:
        query.answer(constants.BAD_RESPONSE_MESSAGE)
        return

    output_message = helpers.create_match_detail_message(response)

    query.answer()
    query.message.edit_text(output_message, parse_mode="MarkdownV2", disable_web_page_preview=True)