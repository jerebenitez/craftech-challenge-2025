# Stage 1
FROM node:18-alpine AS build

WORKDIR /app

COPY . .

RUN npm install && npm run build

# Stage 2
FROM nginx:stable-alpine AS production

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
