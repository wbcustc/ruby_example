class Event < ActiveRecord::Base
  has_many :tag_to_events
  scope :sorted, lambda { order("events.event_at ASC")}
  scope :after, lambda { where("events.event_at >= ?",DateTime.now)}
end
