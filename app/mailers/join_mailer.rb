class JoinMailer < ApplicationMailer
  def join_email_sender(event)
    puts 'enter function'
    @event1 = event
    @time_str = DateTime.parse(Time.at(@event1.event_at.to_f / 1000).to_s).strftime('%b %e %Y at %l:%M %p')
    mail to: "victorwang.bc@gmail.com", subject: "Joining Confirmation"
  end
end
