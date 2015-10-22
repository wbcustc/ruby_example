json.array!(@tags) do |tag|
  json.extract! tag, :id, :tag_name, :photo_url
  json.url tag_url(tag, format: :json)
end
