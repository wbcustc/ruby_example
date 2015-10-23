class EventsController < ApplicationController
  before_action :set_event, only: [:show, :edit, :update, :destroy]

  # GET /events
  # GET /events.json
  def index
    @events = Event.all.after.sorted
    #JoinMailer.send_join_email(@events[0]).deliver
    @tag_dict = Hash.new
    tags = Tag.all
    tags.each do |tag|
      @tag_dict[tag.tag_name] = '../../images/' + tag.photo_url
    end
  end

  # GET /events/1
  # GET /events/1.json
  def show
  end

  # GET /events/new
  # def new
  #   @event = Event.new
  # end

  # GET /events/1/edit
  # def edit
  # end

  # POST /events
  # POST /events.json
  def create
    @event = Event.new(event_params)
    respond_to do |format|
      if @event.save
        tags = params[:tags]
        event_id = @event.id
        valid_tags = Tag.all.select(:tag_name)
        tag_names = Array.new
        valid_tags.each do |valid_tag|
          tag_names.append(valid_tag.tag_name)
        end
        tags.each do |tag|
          if tag_names.include?tag
            TagToEvent.new(tag_name:tag, event_id:event_id).save
          end
        end

        format.html { redirect_to @event, notice: 'Event was successfully created.' }
        format.json { render :show, status: :created, location: @event }
      else
        format.html { render :new }
        format.json { render json: @event.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /events/1
  # PATCH/PUT /events/1.json
  # def update
  #   respond_to do |format|
  #     if @event.update(event_params)
  #       format.html { redirect_to @event, notice: 'Event was successfully updated.' }
  #       format.json { render :show, status: :ok, location: @event }
  #     else
  #       format.html { render :edit }
  #       format.json { render json: @event.errors, status: :unprocessable_entity }
  #     end
  #   end
  # end

  # DELETE /events/1
  # DELETE /events/1.json
  # def destroy
  #   @event.destroy
  #   respond_to do |format|
  #     format.html { redirect_to events_url, notice: 'Event was successfully destroyed.' }
  #     format.json { head :no_content }
  #   end
  # end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_event
      @event = Event.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def event_params
      params.require(:event).permit(:title, :address, :event_at, :lat, :lng, :description, :special_instructions)
    end
end
