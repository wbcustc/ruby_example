class Event < ActiveRecord::Base
  has_many :tag_to_events
end
