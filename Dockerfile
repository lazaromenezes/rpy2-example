from rpy2/jupyter

USER root

RUN chown -R "${NB_USER}" /usr/local/lib/R/site-library

USER $NB_USER

