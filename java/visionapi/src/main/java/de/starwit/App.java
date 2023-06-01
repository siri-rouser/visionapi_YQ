package de.starwit;

import java.util.HexFormat;

import com.google.protobuf.ByteString;
import com.google.protobuf.InvalidProtocolBufferException;

import de.starwit.visionapi.Detector.BoundingBox;
import de.starwit.visionapi.Detector.Detection;
import de.starwit.visionapi.Detector.DetectionOutput;
import de.starwit.visionapi.Videosource.Shape;
import de.starwit.visionapi.Videosource.VideoFrame;

public class App {
    public static void main(String[] args) {
        System.out.println("Testing generated classes");

        // VideoSource classes

        // fake an image
        byte[] bytes = HexFormat.of().parseHex("e04fd020ea3a6910a2d808002b30309d");               
        
        Shape shape1 = Shape.newBuilder()
            .setHeight(1080)
            .setWidth(1920)
            .setChannels(3)
            .build();

        VideoFrame vf = VideoFrame.newBuilder()
            .setShape(shape1)
            .setFrameData(ByteString.copyFrom(bytes))
            .build();

        byte[] serializedObjects = vf.toByteArray();
        System.out.println("Serialized objects " + serializedObjects);

        try {
            VideoFrame parsedVF = VideoFrame.parseFrom(serializedObjects);
            System.out.println(parsedVF.getShape().getHeight());
        } catch(InvalidProtocolBufferException e) {
            System.out.println("can't parse protobuf from bytes");
        }

        // Detector
        BoundingBox bb =  BoundingBox.newBuilder()
            .setMinX(1)
            .setMinY(1)
            .setMaxX(10)
            .setMaxY(10)
            .build();
        Detection d = Detection.newBuilder()
            .setBoundingBox(bb)
            .setConfidence((float)0.5)
            .setClassId(0)
            .build();

        DetectionOutput deOut = DetectionOutput.newBuilder()
            .addDetections(d)
            .build();

        serializedObjects = deOut.toByteArray();
        
        try {
            DetectionOutput parsedDeOut = DetectionOutput.parseFrom(serializedObjects);
            System.out.println(parsedDeOut.getDetections(0).getConfidence());
        } catch (InvalidProtocolBufferException e) {
            System.out.println("can't parse protobuf from bytes");
        }


        // Tracker

    }
}
