class Api::V1::UsersController < ApplicationController
  before_action :set_mail, only: [:new]
  before_action :set_phone_number, only: [:new_with_phone_number]
  before_action :set_password, only: [:new_with_phone_number, :new]
  include ActionController::Cookies
  
  def new
    if @email.blank? || @password.blank?
      render json: { error: 'Password o Email incompleto.' }
    elsif User.where(email: @email).take
      render json: { error: 'No se pudo registrar. El email ya esta registrado.' }
    else
      @user = User.create(email: @email, password: @password)
      send_code_by_mail
      cookies[:user_id] = @user.id
      render json: { msg: 'Usuario creado correctamente.' }, status: 200
    end
  end

  def new_with_phone_number
    if @phone_number.blank? || @password.blank?
      render json: { error: 'Password o Numero de telefono incompleto.' }
    elsif User.where(phone_number: @phone_number).take
      render json: { error: 'No se pudo registrar. El numero de telefono ya esta registrado.' }
    else
      User.create(phone_number: @phone_number, password: @password)
      render json: { msg: 'Usuario creado correctamente.' }, status: 200
    end
  end

  def validation_code
    @user = User.find(cookies[:user_id].to_i)
    if params[:code] == @user.token.token and (Time.now - @user.token.created_at < 600)
      @user.email_verified = true
      @user.token.delete
      @user.save
      render json: { msg: 'Codigo validado correctamente' }, status: 200
    else
      render json: { error: 'No se pudó validar.' }
    end
  end

  private

  def send_code_by_mail
    code = SecureRandom.random_number(10**6).to_s.rjust(6, '0')
    @user.token = Token.new(token: code)
    @user.save
    UserMailer.with(user: @user, code: code).validation_email.deliver_now
  end

  def set_mail
    @email = params[:email]
  end

  def set_password
    @password = params[:password]
  end

  def set_phone_number
    @phone_number = params[:phone_number]
  end
end
