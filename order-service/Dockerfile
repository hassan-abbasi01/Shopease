# Order Service Dockerfile
FROM openjdk:11
WORKDIR /app
COPY . /app
RUN ./mvnw package
CMD ["java", "-jar", "target/order-service.jar"]
