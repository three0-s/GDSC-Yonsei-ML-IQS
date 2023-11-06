FROM nginx
RUN rm /etc/nginx/conf.d/default.conf

COPY public.pem /etc/ssl/certs/public.pem
COPY private.pem /etc/ssl/private/private.pem
COPY nginx.conf /etc/nginx/conf.d/