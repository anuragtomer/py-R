myfunction <- function() {
    a <- rnorm(100)
    mean(a)
}
second <- function(a) {
    rnorm(length(a))
}
