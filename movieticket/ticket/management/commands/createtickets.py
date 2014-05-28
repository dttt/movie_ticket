from django.core.management.base import BaseCommand, CommandError

from ticket.models import Ticket, Schedule, TicketType
from helper.misc import Message
from helper.helper import MiscHelper


class Command(BaseCommand):
    args = '<schedule_id schedule_id ...>'
    help = Message.CREATE_TICKETS_HELP

    def handle(self, *args, **options):
        helper = MiscHelper()
        for schedule_id in args:
            try:
                schedule = Schedule.objects.get(pk=int(schedule_id))
                ticket_type = TicketType.objects.all()[:1].get()
            except Schedule.DoesNotExist:
                raise CommandError('Lich "%s" khong ton tai' % schedule_id)

            total_row = helper.get_alphabet(schedule.room.total_row)
            total_column = schedule.room.total_column

            for row in total_row:
                for column in range(1, total_column + 1):
                    ticket = Ticket(
                        row=row,
                        column=column,
                        schedule=schedule,
                        ticket_type=ticket_type
                    )
                    ticket.save()

            self.stdout.write('Successfully create tickets for schedule "%s"' % schedule_id)
