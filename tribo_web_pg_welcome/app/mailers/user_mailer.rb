class UserMailer < ApplicationMailer
  default from: 'tribo@gmail.com'
  def validation_email
    @user = params[:user]
    @code = params[:code]
    mail(to: @user.email, subject: 'Code verification')
  end
end
