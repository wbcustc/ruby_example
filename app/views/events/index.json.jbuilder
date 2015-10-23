json.array!(@events) do |event|
  json.extract! event, :id, :title, :address, :event_at, :lat, :lng
  #json.url event_url(event, format: :json)
end
