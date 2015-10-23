class JoinMailer < ApplicationMailer
  def join_email_sender(event)
    @event = event
    @time_str = DateTime.parse(Time.at(@event.event_at.to_f / 1000).to_s).strftime('%c')
    mail to: "victorwang.bc@gmail.com", subject: "Joining Confirmation"
  end
end
