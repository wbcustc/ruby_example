class CreateTagToEvents < ActiveRecord::Migration
  def change
    create_table :tag_to_events do |t|
      t.string :tag_name
      t.references :event
      t.timestamps null: false
    end
  end
end
