class AppFailure {
  final String message;
  AppFailure([this.message = "Sorry, some unexpected occured!"]);

  @override
  String toString() => "AppFailure(message: $message)";
}
