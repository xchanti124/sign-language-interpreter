function predictedSign = classify_sign(landmarks)

    persistent net;
    if isempty(net)
        load('./trained_network.mat', 'net');
    end

    predictedSign = char(classify(net, landmarks));

end